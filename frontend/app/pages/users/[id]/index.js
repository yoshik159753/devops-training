import Layout from "../../../components/layout";
import getUserById from "../../../actions";

const User = (props) => {
  const user = props.user;

  return (
    <Layout pageTitle="User">
      {user.id}, {user.name}, {user.email}, {user.created_at}, {user.updated_at}
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
