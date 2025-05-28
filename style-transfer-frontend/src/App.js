import React, { useState } from "react";
import "./App.css";

function App() {
  const [contentImage, setContentImage] = useState(null);
  const [styleImage, setStyleImage] = useState(null);
  const [resultImage, setResultImage] = useState(null);
  const [size, setSize] = useState(512);
  const [steps, setSteps] = useState(300);
  const [styleWeight, setStyleWeight] = useState(1e5);
  const [contentWeight, setContentWeight] = useState(1);
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
    formData.append("style_weight", styleWeight);
    formData.append("content_weight", contentWeight);

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

  const handleDownload = () => {
    if (!resultImage) return;
    
    const link = document.createElement('a');
    link.href = resultImage;
    const date = new Date();
    const timestamp = `${date.getFullYear()}-${(date.getMonth()+1).toString().padStart(2, '0')}-${date.getDate().toString().padStart(2, '0')}_${date.getHours().toString().padStart(2, '0')}-${date.getMinutes().toString().padStart(2, '0')}-${date.getSeconds().toString().padStart(2, '0')}`;
    link.download = `style-transfer-${timestamp}.jpg`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="app-wrapper">
    <h1>Style Transfer</h1>

    <div className="main-content">
      {/* Левый блок - форма */}
      <div className="form-column">
        <form onSubmit={handleSubmit}>
          <div className="upload-section">
            <div className="upload-block">
              <label htmlFor="content">Контентное изображение</label>
              <input
                type="file"
                id="content"
                accept="image/*"
                onChange={(e) => setContentImage(e.target.files[0])}
              />
            </div>

            <div className="upload-block">
              <label htmlFor="style">Изображение стиля</label>
              <input
                type="file"
                id="style"
                accept="image/*"
                onChange={(e) => setStyleImage(e.target.files[0])}
              />
            </div>
          </div>

          <div className="image-preview-container">
            {contentImage ? (
              <div className="image-preview">
                <img
                  src={URL.createObjectURL(contentImage)}
                  alt="Content Preview"
                  className="preview-image"
                />
              </div>
            ) : (
              <div className="image-preview" style={{ background: '#eef2ff' }}></div>
            )}

            {styleImage ? (
              <div className="image-preview">
                <img
                  src={URL.createObjectURL(styleImage)}
                  alt="Style Preview"
                  className="preview-image"
                />
              </div>
            ) : (
              <div className="image-preview" style={{ background: '#eef2ff' }}></div>
            )}
          </div>

          <div className="params-row">
            <div className="param-group">
              <label htmlFor="size">Размер изображения</label>
              <input
                type="number"
                id="size"
                value={size}
                onChange={(e) => setSize(e.target.value)}
                min="128"
                max="1024"
              />
            </div>

            <div className="param-group">
              <label htmlFor="steps">Шаги обработки</label>
              <input
                type="number"
                id="steps"
                value={steps}
                onChange={(e) => setSteps(e.target.value)}
                min="1"
                max="1000"
              />
            </div>
          </div>

          <div className="params-row">
            <div className="param-group">
              <label htmlFor="style-weight">Вес стиля (×10⁵)</label>
              <input
                type="number"
                id="style-weight"
                value={styleWeight / 1e5}
                onChange={(e) => setStyleWeight(e.target.value * 1e5)}
                min="0.1"
                max="10"
                step="0.01"
              />
            </div>

            <div className="param-group">
              <label htmlFor="content-weight">Вес контента</label>
              <input
                type="number"
                id="content-weight"
                value={contentWeight}
                onChange={(e) => setContentWeight(e.target.value)}
                min="1"
                max="10"
                step="1"
              />
            </div>
          </div>

          <button type="submit" disabled={loading}>
            {loading ? (
              <>
                Обработка
                <span className="loader"></span>
              </>
            ) : (
              "Обработать"
            )}
          </button>

          {error && <div className="error-message">{error}</div>}
        </form>
      </div>

      {/* Правый блок - результат */}
      <div className="result-column">
        <div className="result-panel">
          <h2 className="result-title">Результат</h2>
          <div className="result-image-container">
            {loading && (
              <div className="loading-overlay">
                <span>Идёт обработка ...</span>
                <span className="loader"></span>
              </div>
            )}
            
            {resultImage ? (
              <img
                src={resultImage}
                alt="Stylized Result"
                className="result-image"
                onClick={handleDownload}
              />
            ) : (
              <div className="result-placeholder">
                Здесь появится результат
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  </div>
);
}

export default App;