import React, { useEffect, useState } from "react";
import { createRoot } from "react-dom/client";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer } from "recharts";
import "./styles.css";

const API = "http://127.0.0.1:8000";

function App() {
  const [tab, setTab] = useState("analyzer");
  const [form, setForm] = useState({
    sender: "training@example.org",
    subject: "Cybersecurity Workshop Reminder",
    body: "This is a normal informational reminder for the scheduled cybersecurity workshop.",
    attachment_name: ""
  });
  const [result, setResult] = useState(null);
  const [stats, setStats] = useState(null);
  const [history, setHistory] = useState([]);
  const [indicators, setIndicators] = useState([]);
  const [error, setError] = useState("");

  async function loadDashboard() {
    try {
      const [s, h, i] = await Promise.all([
        fetch(`${API}/api/dashboard/stats`).then(r => r.json()),
        fetch(`${API}/api/analyses`).then(r => r.json()),
        fetch(`${API}/api/dashboard/indicators`).then(r => r.json())
      ]);
      setStats(s); setHistory(h); setIndicators(i);
    } catch {
      setError("Backend is not reachable. Start FastAPI on port 8000.");
    }
  }

  useEffect(() => { loadDashboard(); }, []);

  async function analyze() {
    setError(""); setResult(null);
    try {
      const r = await fetch(`${API}/api/analyze`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(form)
      });
      const data = await r.json();
      if (!r.ok) throw new Error(data.detail || "Analysis failed");
      setResult(data);
      loadDashboard();
    } catch (e) {
      setError(e.message);
    }
  }

  const demoPhishing = () => setForm({
    sender: "security-alert@account-check.invalid.test",
    subject: "URGENT: Verify Your Account Immediately",
    body: "Immediately verify your password or your account will be suspended. Visit http://198.51.100.10/verify-account",
    attachment_name: "invoice.pdf.exe"
  });

  return (
    <div className="app">
      <aside className="sidebar">
        <div className="brand">
          <div className="brand-mark">PD</div>
          <div><strong>PhishGuard</strong><small>Defensive Email Analysis</small></div>
        </div>
        {["analyzer", "dashboard", "history", "awareness"].map(x =>
          <button className={tab === x ? "nav active" : "nav"} onClick={() => setTab(x)} key={x}>
            {x[0].toUpperCase() + x.slice(1)}
          </button>
        )}
        <div className="safe-note">
          Synthetic / authorized data only.<br/>
          URLs are analyzed statically and never opened.
        </div>
      </aside>

      <main className="main">
        <header className="topbar">
          <div><h1>Phishing Email Detection & Awareness Dashboard</h1>
          <p>Explainable, defensive analysis for student cybersecurity proof of work.</p></div>
          <span className="status">DEFENSIVE MODE</span>
        </header>

        {error && <div className="error">{error}</div>}

        {tab === "analyzer" && <section>
          <div className="section-head">
            <div><h2>Email Analyzer</h2><p>Analyze sender, content, URLs and attachment filenames.</p></div>
            <button className="secondary" onClick={demoPhishing}>Load safe phishing demo</button>
          </div>
          <div className="grid-two">
            <div className="card form-card">
              <label>Sender<input value={form.sender} onChange={e=>setForm({...form,sender:e.target.value})}/></label>
              <label>Subject<input value={form.subject} onChange={e=>setForm({...form,subject:e.target.value})}/></label>
              <label>Body<textarea rows="10" value={form.body} onChange={e=>setForm({...form,body:e.target.value})}/></label>
              <label>Attachment filename (optional)<input value={form.attachment_name} onChange={e=>setForm({...form,attachment_name:e.target.value})}/></label>
              <button className="primary" onClick={analyze}>ANALYZE EMAIL</button>
            </div>
            <div className="card result-card">
              {!result ? <div className="empty"><h3>No analysis yet</h3><p>Enter a safe sample or load the demonstration.</p></div> :
                <>
                  <div className="score-row"><div><small>PHISHING RISK SCORE</small><div className="score">{result.risk_score}/100</div></div><div className="classification">{result.classification}</div></div>
                  <div className="columns">
                    <Finding title="Sender Analysis" items={result.sender_findings}/>
                    <Finding title="Content Analysis" items={result.content_findings}/>
                    <Finding title="Attachment Analysis" items={result.attachment_findings}/>
                    <Finding title="URL Analysis" items={result.url_results.flatMap(x => x.findings.map(f => `${x.url}: ${f}`))}/>
                  </div>
                  <Finding title="Why it may be suspicious" items={result.indicators.map(x => x.description)}/>
                  <Finding title="Recommended Actions" items={result.recommendations}/>
                </>
              }
            </div>
          </div>
        </section>}

        {tab === "dashboard" && <Dashboard stats={stats} indicators={indicators}/>}
        {tab === "history" && <History history={history}/>}
        {tab === "awareness" && <Awareness/>}
      </main>
    </div>
  );
}

function Finding({title, items}) {
  return <div className="finding"><h3>{title}</h3>{items?.length ? <ul>{items.map((x,i)=><li key={i}>{x}</li>)}</ul> : <p>None detected.</p>}</div>
}

function Dashboard({stats, indicators}) {
  const cards = [
    ["Total Emails Analyzed", stats?.total_emails ?? 0],
    ["Likely Phishing", stats?.likely_phishing ?? 0],
    ["Suspicious", stats?.suspicious ?? 0],
    ["Low / Moderate", stats?.low_risk ?? 0],
    ["Average Risk", stats?.average_risk_score ?? 0]
  ];
  return <section><div className="section-head"><div><h2>Security Analytics</h2><p>Stored analysis metadata and detected indicators.</p></div></div>
    <div className="cards">{cards.map(([a,b])=><div className="metric card" key={a}><small>{a}</small><strong>{b}</strong></div>)}</div>
    <div className="card chart-card"><h3>Top Detected Indicators</h3>
      <ResponsiveContainer width="100%" height={320}><BarChart data={indicators}><XAxis dataKey="indicator"/><YAxis/><Tooltip/><Bar dataKey="count"/></BarChart></ResponsiveContainer>
    </div>
  </section>
}

function History({history}) {
  return <section><h2>Analysis History</h2><p>Only safe analysis metadata is stored by default.</p>
    <div className="card table-wrap"><table><thead><tr><th>ID</th><th>Domain</th><th>Subject</th><th>Risk</th><th>Classification</th><th>Time</th></tr></thead>
      <tbody>{history.map(x=><tr key={x.analysis_id}><td>{x.analysis_id}</td><td>{x.sender_domain}</td><td>{x.subject}</td><td>{x.risk_score}</td><td>{x.classification}</td><td>{new Date(x.created_at).toLocaleString()}</td></tr>)}</tbody>
    </table></div>
  </section>
}

function Awareness() {
  const points = ["Check the sender address", "Inspect domain spelling", "Treat unexpected urgency carefully", "Hover/check links without opening them", "Never send credentials by email", "Be cautious with unexpected attachments", "Do not trust generic greetings automatically", "Verify unusual payment requests", "Notice threatening language", "Consider the full business context"];
  return <section><h2>How to Spot a Phishing Email</h2><p>Before You Click checklist.</p>
    <div className="awareness-grid">{points.map((p,i)=><div className="card awareness" key={p}><span>{i+1}</span><strong>{p}</strong></div>)}</div>
    <div className="card"><h3>Remember</h3><p>No single indicator proves an email is phishing. Use multiple signals and verify important requests through a trusted channel.</p></div>
  </section>
}

createRoot(document.getElementById("root")).render(<App/>);
