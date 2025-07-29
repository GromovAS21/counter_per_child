let socket;

function connectWebSocket() {
    socket = new WebSocket(
        'ws://' + window.location.host + '/ws/updates/'
    );

    socket.onopen = function(e) {
        console.log('WebSocket connection established');
    };

    socket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        document.getElementById('girlCardTotal').textContent = data.data[1].total;
        document.getElementById('boyCardTotal').textContent = data.data[0].total;

        highlightCardWithHigherTotal();
    };

    socket.onclose = function(e) {
        console.log('WebSocket connection closed, attempting to reconnect...');
        setTimeout(connectWebSocket, 3000);
    };

    socket.onerror = function(e) {
        console.error('WebSocket error:', e);
    };
}