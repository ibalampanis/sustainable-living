import logo from './logo.svg';
import './App.css';
import CardPost from "./components/CardPost";
function App() {
  return (
    <div className="App" >
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          <code>A sipmple UI for sustainable-living-project</code>
        </p>
        <div className="pageWrapper d-lg-flex">
        <CardPost/>
        </div>
      </header>
    </div>
  );
}

export default App;
