import express from "express";
import axios from "axios";
import cors from "cors";
import dotenv from "dotenv";

dotenv.config(); // .env 파일에서 환경 변수 로드

const app = express();
const PORT = 3000;

app.use(cors());

app.get("/search", async (req, res) => {
  const query = req.query.q;
  const clientId = process.env.NAVER_CLIENT_ID || "MfdcTW3d3sRK8fWsYQLM";
  const clientSecret = process.env.NAVER_CLIENT_SECRET || "NROHPJds2g";

  if (!clientId || !clientSecret) {
    return res.status(500).send("API credentials are missing");
  }

  const url = `https://openapi.naver.com/v1/search/blog.json?query=${encodeURIComponent(
    query
  )}`;

  try {
    const response = await axios.get(url, {
      headers: {
        "X-Naver-Client-Id": clientId,
        "X-Naver-Client-Secret": clientSecret,
      },
    });
    res.json(response.data);
  } catch (error) {
    console.error("API 요청 실패:", error.response?.data || error.message);
    res.status(error.response?.status || 500).send(error.message);
  }
});

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Server is running on http://0.0.0.0:${PORT}`);
});
