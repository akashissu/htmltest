# zero-human-sandbox-two

## Frontend demos

This repository includes standalone frontend UI examples:
- `calculator.html`
- `weather-widget.html`
- `modal-component.html`

Open any of these files directly in a browser to preview the component.

## Backend routes

This repository now includes a minimal Node.js backend server with health-check and ping endpoints.

### Install

```bash
npm install
```

### Run

```bash
npm start
```

### Development mode

```bash
npm run dev
```

### Quick validation

```bash
npm test
```

### Health-check endpoint

```bash
curl http://localhost:3000/health
```

Expected response:

```json
{
  "status": "ok"
}
```

### Ping endpoint

```bash
curl http://localhost:3000/ping
```

Expected response:

```json
{
  "pong": true
}
```

### Port note

If port `3000` is already busy in your environment, you can run the server on another port:

```bash
PORT=3100 npm start
```
