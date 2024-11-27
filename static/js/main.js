async function fetchData(endpoint, payload = {}) {
    console.log(`Fetching data from ${endpoint}...`);
    const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
    });
    if (!response.ok) {
        console.error(`Error fetching data from ${endpoint}: ${response.statusText}`);
        return [];
    }
    const data = await response.json();
    console.log(`Data received from ${endpoint}:`, data);
    return data;
}

function renderChart(chartId, type, labels, data, title) {
    if (Chart.getChart(chartId)) {
        Chart.getChart(chartId).destroy(); 
    }

    const ctx = document.getElementById(chartId).getContext("2d");
    new Chart(ctx, {
        type,
        data: {
            labels,
            datasets: [
                {
                    label: title,
                    data,
                    backgroundColor: "rgba(75, 192, 192, 0.2)",
                    borderColor: "rgba(75, 192, 192, 1)",
                    borderWidth: 1,
                },
            ],
        },
        options: {
            responsive: true,
            plugins: {
                title: {
                    display: true,
                    text: title,
                },
            },
            scales: {
                y: { beginAtZero: true },
            },
        },
    });
}

async function fetchAndRenderChart(apiEndpoint, chartId, chartType, chartTitle, labelKey, dataKey) {
    const data = await fetchData(apiEndpoint);
    if (data.length === 0) {
        console.warn(`No data returned for ${chartId}`);
        return;
    }
    const labels = data.map((item) => item[labelKey]);
    const values = data.map((item) => item[dataKey]);
    renderChart(chartId, chartType, labels, values, chartTitle);
}
