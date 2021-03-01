import logo from '../../logo.svg';
import './App.css';

import Comments from '../Comments/Comments';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      </header>
      <main className="App-main">
        <Comments />
      </main>
    </div>
  );
}

export default App;
