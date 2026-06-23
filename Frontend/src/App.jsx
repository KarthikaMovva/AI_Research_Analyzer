import { useState } from "react";
import API from "./services/api";

import QueryBox from "./component/QueryBox";
import ReportViewer from "./component/Report";

import "./App.css";

function App() {

  const [report, setReport] = useState("");
  const [loading, setLoading] = useState(false);

  const generateReport = async (query) => {

    setLoading(true);

    try {

      const response = await API.post(
        "/research",
        { query }
      );

      setReport(response.data.report);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);
    }
  };

  return (
    <div className="app">

      <div className="container">

        <div className="header">

          <h1>AI Research Analyzer</h1>

          <p>
            Generate accurate, structured research reports using AI.
          </p>

        </div>

        <div className="query-section">
          <QueryBox onSubmit={generateReport} />
        </div>

        {loading && (
          <div className="loading">
            Generating Research Report...
          </div>
        )}

        {report && (
          <div className="report-section">

            <h2>Research Report</h2>

            <ReportViewer report={report} />

          </div>
        )}

      </div>

    </div>
  );
}

export default App;