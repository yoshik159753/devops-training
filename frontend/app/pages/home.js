import Layout from "../components/layout";

const Home = () => {
  return (
    <Layout pageTitle="Home">
      <main>
        <h1>Sample App</h1>
        <p>
          This is the home page for the
          <a href="https://railstutorial.jp/">Ruby on Rails Tutorial</a>
          sample application.
        </p>
      </main>
    </Layout>
  );
};

export default Home;
