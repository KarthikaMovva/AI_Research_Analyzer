import { useState } from "react";
import API from "./services/api";

import QueryBox from "./component/QueryBox";
import ReportViewer from "./component/Report";

import "./App.css";


function App() {

  const [file, setFile] = useState(null);

  const [uploadedFile, setUploadedFile] = useState("");

  const [report, setReport] = useState("");

  const [loading, setLoading] = useState(false);

  const [uploading, setUploading] = useState(false);



  const uploadDocument = async () => {


    if (!file) {
      alert("Select a document first");
      return;
    }


    const formData = new FormData();

    formData.append(
      "file",
      file
    );


    setUploading(true);


    try {

      const response = await API.post(
        "/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        }
      );


      setUploadedFile(
        response.data.filename
      );


    }
    catch (error) {

      console.log(error);

    }
    finally {

      setUploading(false);

    }

  };





  const generateReport = async (query) => {


    setLoading(true);


    try {


      const response = await API.post(
        "/research",
        {
          query
        }
      );


      setReport(
        response.data.report
      );


    }
    catch (error) {

      console.log(error);

    }
    finally {

      setLoading(false);

    }

  };





  return (

    <div className="page">


      <div className="navbar">

        <h2>
          AI Research Analyzer
        </h2>


        <span>
          Intelligent Document Research Assistant
        </span>


      </div>



      <div className="main-container">



        <section className="hero">


          <h1>
            Transform Documents into Insights
          </h1>


          <p>
            Upload research papers, PDFs or documents and interact with them using AI-powered research agents.
          </p>


        </section>





        <section className="upload-card">


          <div className="card-header">

            <h3>
              Knowledge Source
            </h3>


            <p>
              Upload your document to create an AI knowledge base.
            </p>

          </div>




          <div className="upload-area">


            <input

              type="file"

              onChange={(e) =>
                setFile(e.target.files[0])
              }

            />


            <button

              onClick={uploadDocument}

            >

              {
                uploading
                  ?
                  "Processing..."
                  :
                  "Upload Document"
              }


            </button>


          </div>



          {
            uploadedFile &&

            <div className="status">


              <span>
                ✓
              </span>


              {uploadedFile} indexed successfully


            </div>

          }



        </section>







        <section className="chat-card">


          <div className="card-header">

            <h3>
              Ask your document
            </h3>


            <p>
              Ask questions and get AI-generated answers.
            </p>

          </div>



          <QueryBox

            onSubmit={generateReport}

          />



        </section>






        {
          loading &&

          <div className="loading-card">

            <div className="spinner"></div>

            Analyzing document...


          </div>

        }






        {
          report &&

          <section className="answer-card">


            <div className="answer-title">

              <h3>
                AI Response
              </h3>


            </div>


            <ReportViewer

              report={report}

            />


          </section>

        }



      </div>

    </div>

  );

}


export default App;