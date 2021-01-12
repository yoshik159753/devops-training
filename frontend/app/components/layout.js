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
      </Head>

      <header className="navbar navbar-fixed-top navbar-inverse">
        <div className="container">
          <Link href="#" id="logo">
            sample app
          </Link>
          <nav>
            <ul className="nav navbar-nav navbar-right">
              <li>
                <Link href="#">Home</Link>
              </li>
              <li>
                <Link href="#">Help</Link>
              </li>
              <li>
                <Link href="#">Log in</Link>
              </li>
            </ul>
          </nav>
        </div>
      </header>

      <div className="container">
        <main>{props.children}</main>
      </div>
    </div>
  );
}
