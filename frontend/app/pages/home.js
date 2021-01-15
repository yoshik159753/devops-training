import Link from "next/link";
import Layout from "../components/layout";

const Home = () => {
  return (
    <Layout pageTitle="Home">
      <div className="center jumbotron">
        <h1>Welcome to the Sample App</h1>
        <h2>
          This is the home page for the
          <Link href="https://railstutorial.jp/">Ruby on Rails Tutorial</Link>
          sample application.
        </h2>
        <Link href="/signup">
          <a className="btn btn-lg btn-primary">Sign up now!</a>
        </Link>
      </div>

      <Link href="http://rubyonrails.org/">
        <img
          className="d-block img-fluid"
          src="/images/rails.png"
          alt="Rails logo"
        />
      </Link>
    </Layout>
  );
};

export default Home;
