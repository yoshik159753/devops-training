import React from "react";

export default function ErrorMessages({ messages }) {
  if (messages.length <= 0) {
    return <React.Fragment />;
  }

  return (
    <div id="error_explanation">
      <div class="alert alert-danger">
        The form contains {messages.length} error(s).
      </div>
      <ul>
        {messages.map((message) => (
          <li>{message}</li>
        ))}
      </ul>
    </div>
  );
}
