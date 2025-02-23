const express = require("express");
const axios = require("axios");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());
app.use(require("cors")());

const FLASK_API_URL = "http://127.0.0.1:5000/predict";

app.post("/analyze-sentiment", async (req, res) => {
    try {
        const { text } = req.body;
        if (!text) {
            return res.status(400).json({ error: "Text field is required" });
        }

        const response = await axios.post(FLASK_API_URL, { text });
        res.json(response.data);
    } catch (error) {
        res.status(500).json({ error: "Error connecting to sentiment analysis API" });
    }
});

app.listen(3000, () => {
    console.log("Express server running on port 3000");
});
