import React from "react";
import Link from "next/link";

export default function Footer() {
  return (
    <React.Fragment>
      <footer className="footer">
        <small>
          The <a href="https://railstutorial.jp/">Ruby on Rails Tutorial</a>
          by <a href="http://www.michaelhartl.com/">Michael Hartl</a>
        </small>
        <nav>
          <ul>
            <li>
              <Link href="#">About</Link>
            </li>
            <li>
              <Link href="#">Contact</Link>
            </li>
            <li>
              <Link href="http://news.railstutorial.org/">News</Link>
            </li>
          </ul>
        </nav>
      </footer>
    </React.Fragment>
  );
}
