import Layout from "../components/layout";

const Signup = () => {
  return (
    <Layout pageTitle="Sign up">
      <h1>Sign up</h1>

      <form>
        <div className="form-group">
          <label htmlFor="name">Name</label>
          <input
            value=""
            name="name"
            type="text"
            className="form-control"
            id="name"
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            value=""
            name="email"
            type="email"
            className="form-control"
            id="email"
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            value=""
            name="password"
            type="password"
            className="form-control"
            id="password"
          />
        </div>
        <div className="form-group">
          <label htmlFor="passwordConfirmation">Confirmation</label>
          <input
            value=""
            name="passwordConfirmation"
            type="password"
            className="form-control"
            id="passwordConfirmation"
          />
        </div>
        <div className="form-group">
          <button
            onClick="#"
            type="button"
            className="btn btn-primary form-control"
          >
            Create my account
          </button>
        </div>
      </form>
    </Layout>
  );
};

export default Signup;
