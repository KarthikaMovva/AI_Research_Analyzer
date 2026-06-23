import { useState } from "react";

export default function QueryBox({ onSubmit }) {

    const [query, setQuery] = useState("");

    return (

        <div>

            <textarea
                value={query}
                onChange={(e) =>
                    setQuery(e.target.value)
                }
                placeholder="Ask a research question..."
                rows="5"
                className="query-input"
            />

            <button
                className="generate-btn"
                onClick={() => onSubmit(query)}
            >
                Generate Report
            </button>

        </div>
    );
}