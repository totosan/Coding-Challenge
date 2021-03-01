import React from 'react';
import './Comments.css';

import AddComment from './AddComment';

class Comments extends React.Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div className="Comments">
        <AddComment />
      </div>
    );
  }
}

export default Comments;
