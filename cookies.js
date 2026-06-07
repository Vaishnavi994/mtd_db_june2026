const http = require('http');

const server = http.createServer((req, res) => {

    // Read cookies from request header
    const cookies = req.headers.cookie;

    if (cookies) {
        res.write("Cookies Found:\n");
        res.write(cookies);
    } else {
        res.write("No Cookies Found");
    }

    res.end();
});

server.listen(3000, () => {
    console.log("Server running at http://localhost:3000");
});