# zero-human-sandbox-two

## Backend health-check

This repository now includes a minimal Node.js backend server with a health-check endpoint.

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
