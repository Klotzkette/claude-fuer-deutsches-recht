import { createServer } from 'node:http'
import { readFile } from 'node:fs/promises'

const port = Number(process.argv[2] ?? 8765)
if (!Number.isInteger(port) || port < 1024 || port > 65535) {
  throw new Error('Erwartet wird ein lokaler Port zwischen 1024 und 65535.')
}

const publicFiles = new Map([
  ['/', ['index.html', 'text/html; charset=utf-8']],
  ['/style.css', ['style.css', 'text/css; charset=utf-8']],
  ['/ui.mjs', ['ui.mjs', 'text/javascript; charset=utf-8']],
  ['/engine.mjs', ['engine.mjs', 'text/javascript; charset=utf-8']],
  ['/beispiel.json', ['beispiel.json', 'application/json; charset=utf-8']],
])

createServer(async (req, res) => {
  if (req.method !== 'GET' && req.method !== 'HEAD') {
    res.writeHead(405, { Allow: 'GET, HEAD' }).end()
    return
  }
  const asset = publicFiles.get(req.url)
  if (!asset) {
    res.writeHead(404).end()
    return
  }
  try {
    const body = await readFile(new URL(asset[0], import.meta.url))
    res.writeHead(200, {
      'Content-Type': asset[1],
      'Cache-Control': 'no-store',
      'X-Content-Type-Options': 'nosniff',
      'Content-Security-Policy': "default-src 'self'; form-action 'none'; frame-ancestors 'none'; base-uri 'none'",
    }).end(req.method === 'HEAD' ? undefined : body)
  } catch {
    res.writeHead(500).end()
  }
}).listen(port, '127.0.0.1', () => {
  process.stdout.write(`Lokales Applet: http://127.0.0.1:${port}\n`)
})
