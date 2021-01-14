import React from "react";
import Link from "next/link";

export default function Header() {
  return (
    <React.Fragment>
      <header>
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
      </header>
    </React.Fragment>
  );
}
