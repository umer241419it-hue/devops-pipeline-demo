from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Pipeline Demo</title>
    <style>
        :root {
            --bg-color: #0f172a;
            --card-bg: #1e293b;
            --text-main: #f8fafc;
            --text-sub: #94a3b8;
            --accent: #38bdf8;
            --accent-green: #22c55e;
            --border-color: #334155;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        }
        body {
            background-color: var(--bg-color);
            color: var(--text-main);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .card {
            background-color: var(--card-bg);
            border: 1px solid var(--border-color);
            border-radius: 16px;
            padding: 40px 32px;
            max-width: 600px;
            width: 100%;
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.5), 0 8px 10px -6px rgba(0, 0, 0, 0.5);
            text-align: center;
        }
        .badge-healthy {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(34, 197, 94, 0.15);
            color: var(--accent-green);
            padding: 6px 14px;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 600;
            margin-bottom: 20px;
            border: 1px solid rgba(34, 197, 94, 0.3);
        }
        .status-dot {
            width: 8px;
            height: 8px;
            background-color: var(--accent-green);
            border-radius: 50%;
            box-shadow: 0 0 8px var(--accent-green);
        }
        h1 {
            font-size: 2.25rem;
            font-weight: 700;
            color: var(--text-main);
            margin-bottom: 12px;
            letter-spacing: -0.025em;
        }
        p.subtitle {
            font-size: 1.1rem;
            color: var(--text-sub);
            margin-bottom: 28px;
            line-height: 1.5;
        }
        .pipeline-flow {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
            margin: 24px 0;
            padding: 16px;
            background: rgba(15, 23, 42, 0.6);
            border-radius: 12px;
            border: 1px solid var(--border-color);
        }
        .step {
            background: #2d3748;
            padding: 6px 12px;
            border-radius: 8px;
            font-size: 0.85rem;
            font-weight: 500;
            color: #e2e8f0;
        }
        .arrow {
            color: var(--accent);
            font-size: 0.9rem;
        }
        .meta-info {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin-top: 24px;
            padding-top: 20px;
            border-top: 1px solid var(--border-color);
        }
        .meta-item {
            text-align: left;
            background: rgba(15, 23, 42, 0.4);
            padding: 10px 14px;
            border-radius: 8px;
        }
        .meta-label {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-sub);
            margin-bottom: 4px;
        }
        .meta-value {
            font-size: 0.9rem;
            font-weight: 600;
            color: var(--text-main);
        }
        .api-link {
            display: inline-block;
            margin-top: 20px;
            color: var(--accent);
            text-decoration: none;
            font-size: 0.9rem;
            font-weight: 500;
            transition: opacity 0.2s;
        }
        .api-link:hover {
            opacity: 0.8;
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <div class="card">
        <div class="badge-healthy">
            <span class="status-dot"></span>
            Pipeline Active & Live
        </div>
        <h1>DevOps Pipeline Demo</h1>
        <p class="subtitle">Application deployed successfully through the DevOps pipeline.</p>
        
        <div class="pipeline-flow">
            <span class="step">Git / GitHub</span>
            <span class="arrow">&rarr;</span>
            <span class="step">Jenkins</span>
            <span class="arrow">&rarr;</span>
            <span class="step">pytest</span>
            <span class="arrow">&rarr;</span>
            <span class="step">Docker Build</span>
            <span class="arrow">&rarr;</span>
            <span class="step">Deploy</span>
        </div>

        <div class="meta-info">
            <div class="meta-item">
                <div class="meta-label">Environment</div>
                <div class="meta-value">Docker Container</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Port</div>
                <div class="meta-value">5000</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Health Check</div>
                <div class="meta-value">HTTP 200 OK</div>
            </div>
            <div class="meta-item">
                <div class="meta-label">Status</div>
                <div class="meta-value" style="color: var(--accent-green);">Healthy</div>
            </div>
        </div>

        <a href="/health" class="api-link" target="_blank">View JSON Health Endpoint &rarr;</a>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE), 200

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "devops-pipeline-demo",
        "message": "Application is running smoothly"
    }), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
