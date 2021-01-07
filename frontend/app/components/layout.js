import Head from "next/head";

function fullTitle(pageTitle = "") {
  const siteTitle = "Ruby on Rails Tutorial Sample App";
  return pageTitle ? pageTitle + " | " + siteTitle : siteTitle;
}

export default function Layout(props) {
  return (
    <div>
      <Head>
        <title>{fullTitle(props.pageTitle)}</title>
      </Head>
      <main>{props.children}</main>
    </div>
  );
}
