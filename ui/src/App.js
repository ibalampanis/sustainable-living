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
          <p>
            Find the original repo on:
            <a href="https://github.com/ibalampanis/sustainable-living">
              <i class="fa-brands fa-github fa-bounce fa-2xl"></i>
            </a>
          </p>
        </p>
        <div className="pageWrapper d-lg-flex">
        <CardPost/>
        </div>
      </header>
    </div>
  );
}

export default App;
