import Layout from "../components/layout";
import { createUser } from "../actions";
import { useState } from "react";
import ErrorMessages from "../components/errorMessages";
import { useRouter } from "next/router";

const Signup = () => {
  const router = useRouter();

  const defaultFormData = {
    name: "",
    email: "",
    password: "",
    password_confirmation: "",
  };

  const [form, setForm] = useState(defaultFormData);
  const [errorMessages, setEerrorMessages] = useState([]);

  const handleChange = (event) => {
    const target = event.target;
    const name = target.name;
    setForm({
      ...form,
      [name]: target.value,
    });
  };

  const submitForm = () => {
    createUser({ ...form })
      .then(({ id }) => {
        router.push(`/users/${id}`);
      })
      .catch(({ response }) => {
        const errors = response.data.errors;
        const messages = errors.map((error) => error["message"]);
        setEerrorMessages(messages);
      });
  };

  return (
    <Layout pageTitle="Sign up">
      <h1>Sign up</h1>

      <form>
        <ErrorMessages messages={errorMessages} />

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
            name="password_confirmation"
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
