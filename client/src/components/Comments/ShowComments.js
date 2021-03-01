import React from 'react';

class ShowComments extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      comments: []
    };

    this.getComments = this.getComments.bind(this);
  }

  componentDidMount() {
    this.getComments();
  }

  render() {
    return (
      <div>
        Kommentare
      </div>
    );
  }

  async getComments() {
  }
}

export default ShowComments;
