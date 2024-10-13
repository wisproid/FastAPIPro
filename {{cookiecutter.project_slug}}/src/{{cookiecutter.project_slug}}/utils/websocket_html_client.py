html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Websocket Test</title>
        <script src="https://cdn.jsdelivr.net/npm/cbor-js@0.1.0/cbor.min.js"></script>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <h2>Your ID: <span id="ws-id"></span></h2>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <form action="" onsubmit="sendMessageCBOR(event)">
            <input type="text" id="messageTextCBOR" autocomplete="off"/>
            <button>Send CBOR</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var client_id = Date.now()
            document.querySelector("#ws-id").textContent = client_id;
            
            var protocol = window.location.hostname === 'localhost' ? 'ws' : window.location.hostname === '127.0.0.1' ? 'ws' : 'wss';
            var port = window.location.port ? `:${window.location.port}` : '';
            var ws = new WebSocket(`${protocol}://${window.location.hostname}${port}/api/v1/ws/testroom/${client_id}`);
            ws.binaryType = "arraybuffer";

            ws.onopen = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode("connected")
                message.appendChild(content)
                messages.appendChild(message)
            };
            ws.onmessage = function(event) {
                if (typeof event.data === 'string') {
                    console.log("Received string data:", event.data);
                } else if (event.data instanceof ArrayBuffer) {
                    console.log("Received binary data (possible CBOR):");
                    var message = CBOR.decode(event.data);
                    console.log(message)
                } else {
                    console.log("Unknown data type received.");
                }
                // var messages = document.getElementById('messages')
                // var message = document.createElement('li')
                // var content = document.createTextNode(event.data)
                // message.appendChild(content)
                // messages.appendChild(message)
            };

            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }

            function sendMessageCBOR(event) {
                var input = document.getElementById("messageTextCBOR")
                var prepare = {mesg: input.value}
                var encoded = CBOR.encode(prepare)
                console.log(encoded)
                ws.send(encoded)
                input.value = ''
                event.preventDefault()

                // var initial = { Hello: "World" };
                // var encodedx = CBOR.encode(initial);
                // console.log(encodedx)
            }

        </script>
    </body>
</html>
"""