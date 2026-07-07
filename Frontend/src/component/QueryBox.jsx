import { useState } from "react";


export default function QueryBox({ onSubmit }) {


    const [query, setQuery] = useState("");



    const submit = () => {

        onSubmit(query);

        setQuery("");

    }



    return (

        <div>


            <textarea

                value={query}

                onChange={(e) =>
                    setQuery(e.target.value)
                }

                placeholder=
                "Ask anything about the uploaded document..."

                rows="5"

                className="query-input"

            />



            <button

                className="generate-btn"

                onClick={submit}

            >

                Ask Question

            </button>


        </div>

    );

}