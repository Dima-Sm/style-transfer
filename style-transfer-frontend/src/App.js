import React, { useState } from "react";
import "./App.css";

function App() {
  const [contentImage, setContentImage] = useState(null);
  const [styleImage, setStyleImage] = useState(null);
  const [resultImage, setResultImage] = useState(null);
  const [size, setSize] = useState(512);
  const [steps, setSteps] = useState(300);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

 const handleSubmit = async (e) => {
  e.preventDefault();

  if (!contentImage || !styleImage) {
    setError("Загрузите оба изображения.");
    return;
  }

  setLoading(true);
  setResultImage(null);
  setError("");

  const formData = new FormData();
  formData.append("content", contentImage);
  formData.append("style", styleImage);
  formData.append("imsize", size);
  formData.append("steps", steps);
  formData.append("style_weight", 1e5); // Или значения из useState
  formData.append("content_weight", 1); // Можно сделать тоже настраиваемыми

  try {
    const response = await fetch("http://localhost:8000/transfer", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.error || data.detail || "Ошибка при обработке");
    }

    if (!data.output_image) {
  throw new Error("Ответ не содержит изображения.");
}
    setResultImage(data.output_image); 
  } catch (err) {
    setError(err.message);
    console.error("Ошибка при отправке:", err);
  } finally {
    setLoading(false);
  }
};

  return (
    <div className="container">
      <h1 className="title"> Style Transfer</h1>

      <form className="form" onSubmit={handleSubmit}>
        <div className="upload-section">
          <div className="upload-block">
            <label htmlFor="content">Контент</label>
            <input
              type="file"
              id="content"
              accept="image/*"
              onChange={(e) => setContentImage(e.target.files[0])}
            />
          </div>

          <div className="upload-block">
            <label htmlFor="style">Стиль</label>
            <input
              type="file"
              id="style"
              accept="image/*"
              onChange={(e) => setStyleImage(e.target.files[0])}
            />
          </div>
        </div>

        <div className="image-preview-container">
          {contentImage && (
            <div className="image-preview">
              <img
                src={URL.createObjectURL(contentImage)}
                alt="Content Preview"
                className="preview-image"
              />
            </div>
          )}
          {styleImage && (
            <div className="image-preview">
              <img
                src={URL.createObjectURL(styleImage)}
                alt="Style Preview"
                className="preview-image"
              />
            </div>
          )}
        </div>

        <div className="input-row">
          <label>
            Размер:
            <input
              type="number"
              value={size}
              onChange={(e) => setSize(e.target.value)}
              min="128"
              max="1024"
            />
          </label>
          <label>
            Шаги:
            <input
              type="number"
              value={steps}
              onChange={(e) => setSteps(e.target.value)}
              min="1"
              max="10"
            />
          </label>
        </div>

        <button type="submit" className="submit-btn" disabled={loading}>
          {loading ? (
            <>
              Обработка
              <span className="loader"></span>
            </>
          ) : (
            "Обработать"
          )}
        </button>
      </form>

      {error && <div className="error-message">{error}</div>}

      {resultImage && (
      <div className="result-block">
        <h2 className="result-title">Результат</h2>
        <img src={resultImage} alt="Stylized" className="result-image" />
      </div>
    )}
    </div>
  );
}

export default App;