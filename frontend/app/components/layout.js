import Head from "next/head";
import Link from "next/link";

function fullTitle(pageTitle = "") {
  const siteTitle = "Ruby on Rails Tutorial Sample App";
  return pageTitle ? pageTitle + " | " + siteTitle : siteTitle;
}

export default function Layout(props) {
  return (
    <div>
      <Head>
        <title>{fullTitle(props.pageTitle)}</title>
        <link
          rel="stylesheet"
          href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
          integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk"
          crossorigin="anonymous"
        ></link>
        <script
          src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
          integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj"
          crossorigin="anonymous"
        ></script>
        <script
          src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
          integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
          crossorigin="anonymous"
        ></script>
        <script
          src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"
          integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI"
          crossorigin="anonymous"
        ></script>
      </Head>

      <nav className="navbar navbar-expand fixed-top navbar-dark bg-dark">
        <div className="container">
          <Link href="#">
            <a className="navbar-brand" href="#" id="logo">
              sample app
            </a>
          </Link>
          <div className="navbar-nav">
            <Link href="#">
              <a className="nav-item nav-link">Home</a>
            </Link>
            <Link href="#">
              <a className="nav-item nav-link">Help</a>
            </Link>
            <Link href="#">
              <a className="nav-item nav-link">Log in</a>
            </Link>
          </div>
        </div>
      </nav>

      <div className="container">
        <main>{props.children}</main>
      </div>
    </div>
  );
}
