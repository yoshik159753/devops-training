import MyHead from "../components/myhead";

const Home = () => {
  return (
    <div>
      <MyHead title="Home" />
      <main>
        <h1>Sample App</h1>
        <p>
          This is the home page for the
          <a href="https://railstutorial.jp/">Ruby on Rails Tutorial</a>
          sample application.
        </p>
      </main>
    </div>
  );
};

export default Home;
