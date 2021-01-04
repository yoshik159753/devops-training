import React from "react";
import Head from "next/head";

const MyHead = (props) => {
  return (
    <React.Fragment>
      <Head>
        <title>{props.title} | Ruby on Rails Tutorial Sample App</title>
      </Head>
    </React.Fragment>
  );
};

export default MyHead;
