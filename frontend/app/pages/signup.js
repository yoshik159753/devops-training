import Layout from "../components/layout";
import { createUser } from "../actions";
import { useState } from "react";

const Signup = () => {
  const defaultFormData = {
    name: "",
    email: "",
    password: "",
    passwordConfirmation: "",
  };

  const [form, setForm] = useState(defaultFormData);

  const handleChange = (event) => {
    const target = event.target;
    const name = target.name;
    setForm({
      ...form,
      [name]: target.value,
    });
  };

  const submitForm = () => {
    createUser({ ...form }).then((res) => {
      console.log(res);
    });
  };

  return (
    <Layout pageTitle="Sign up">
      <h1>Sign up</h1>

      <form>
        <div className="form-group">
          <label htmlFor="name">Name</label>
          <input
            onChange={handleChange}
            value={form.name}
            name="name"
            type="text"
            className="form-control"
            id="name"
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            onChange={handleChange}
            value={form.email}
            name="email"
            type="email"
            className="form-control"
            id="email"
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            onChange={handleChange}
            value={form.password}
            name="password"
            type="password"
            className="form-control"
            id="password"
          />
        </div>
        <div className="form-group">
          <label htmlFor="passwordConfirmation">Confirmation</label>
          <input
            onChange={handleChange}
            value={form.passwordConfirmation}
            name="passwordConfirmation"
            type="password"
            className="form-control"
            id="passwordConfirmation"
          />
        </div>
        <div className="form-group">
          <button
            onClick={submitForm}
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
