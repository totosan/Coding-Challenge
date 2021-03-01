import React from 'react';

class AddComment extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      name: "",
      comment: "",
    };

    this.resetForm = this.resetForm.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  render() {
    const { name, comment } = this.state;

    return (
      <form onSubmit={this.handleSubmit}>
        <label htmlFor="name">Name:</label><br />
        <input id="name" type="text" value={name} onChange={(event) => this.setState({ name: event.target.value })} /><br />
        <label htmlFor="comment">Kommentar:</label><br />
        <textarea id="comment" cols="50" rows="10" value={comment} onChange={(event) => this.setState({ comment: event.target.value })} /><br />
        <button type="button" onClick={this.resetForm}>Reset</button>
        <button>Speichern</button>
      </form>
    );
  }

  resetForm() {
    this.setState({ comment: "" });
  };

  async handleSubmit(event) {
    event.preventDefault();

    const { name, comment } = this.state;
    const response = await fetch('/api/comments', {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ name, comment }),
    });

    const result = await response.json();
    if (result.result === "done") {
      this.resetForm();
      alert("Speichern erfolgreich!");
    } else {
      alert("Fehler beim Speichern!");
    }
  };
}

export default AddComment;
