import Layout from "../components/layout";
import { createUser } from "../actions";
import { useState } from "react";
import ErrorMessages from "../components/errorMessages";
import { useRouter } from "next/router";
import Link from "next/link";

const Login = () => {
  const router = useRouter();

  const defaultFormData = {
    email: "",
    password: "",
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
    // TODO: login とかに書き換え
    // createUser({ ...form })
    //   .then(({ id }) => {
    //     router.push({ pathname: `/users/${id}`, query: { welcome: true } });
    //   })
    //   .catch(({ response }) => {
    //     const errors = response.data.errors;
    //     const messages = errors.map((error) => error["message"]);
    //     setEerrorMessages(messages);
    //   });
  };

  return (
    <Layout pageTitle="Log in">
      <h1>Log in</h1>

      <div className="row">
        <div className="col-md-6 offset-md-3">
          <form>
            <ErrorMessages messages={errorMessages} />

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
              <button
                onClick={submitForm}
                type="button"
                className="btn btn-primary form-control"
              >
                Log in
              </button>
            </div>
          </form>
          <p>
            New user?{" "}
            <Link href="/signup">
              <a>Sign up now!</a>
            </Link>
          </p>
        </div>
      </div>
    </Layout>
  );
};

export default Login;
