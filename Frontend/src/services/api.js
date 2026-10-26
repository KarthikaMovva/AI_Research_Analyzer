import axios from "axios";
// Use the address that the FastAPI server is guaranteed to listen on.
// “localhost” works on Windows even when FastAPI is started with --host 0.0.0.0.
const API = axios.create({
    baseURL: "http://localhost:8000",
});

export default API;