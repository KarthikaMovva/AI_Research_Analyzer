import ReactMarkdown from "react-markdown";

export default function Report({ report }) {

    return (
        <div className="report-content">

            <ReactMarkdown>
                {report}
            </ReactMarkdown>

        </div>
    );
}