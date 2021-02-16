import crypto from "crypto";
import Layout from "../../../components/layout";
import { getUserById } from "../../../actions";
import { useRouter } from "next/router";

const User = (props) => {
  const router = useRouter();

  const user = props.user;
  const hashByEmail = crypto.createHash("md5").update(user.email).digest("hex");
  const gravatarUrl = `https://secure.gravatar.com/avatar/#${hashByEmail}`;

  const { welcome } = router.query;

  return (
    <Layout pageTitle={user.name}>
      {welcome && (
        <div className="alert alert-success">Welcome to the Sample App!</div>
      )}

      <aside className="col-md-4">
        <section className="user_info">
          <h1>
            <img src={gravatarUrl} alt={user.name} className="gravatar" />
            {user.name}
          </h1>
        </section>
      </aside>
      {/* {user.id}, {user.name}, {user.email}, {user.created_at}, {user.updated_at} */}
    </Layout>
  );
};

export async function getServerSideProps(context) {
  const user = await getUserById(context.params.id);
  return {
    props: {
      user: user,
    },
  };
}

export default User;
