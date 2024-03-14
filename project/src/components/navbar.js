import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
    return (
        <nav>
            <ul>
                <li>
                    <Link to="/login">Login</Link>
                </li>
                <li>
                    <Link to="/predict">Predict</Link>
                </li>
            </ul>
        </nav>
    );
}

export default Navbar;
