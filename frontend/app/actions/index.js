import axios from "axios";

const BASE_URL = "http://127.0.0.1:5000";

const getUserById = (id) =>
  axios.get(`${BASE_URL}/api/v1/users/${id}`).then((res) => res.data);

export default getUserById;
