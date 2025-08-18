import {Link} from "react-router";
import { useAuth } from '../AuthContext';

import styles from "./Header.module.css"
const Header = () => {
    const {isAuth } = useAuth();


    return ( 
        <header 
        className={styles.header} >
            <h1> Homestead Tracker </h1>
              <h2> Helping you keep your plants, and calander happy </h2>
            <nav> className={styles.nav}
                <ul>
                    {isAuth ? (
                    <>
                       <li> 
                        <Link to="/" >Home</Link>
                       </li>
                    </>
                    ) : (
                       <>
                          <li> 
                            Crops  
                            {/* this will get replaced by a Link, 
                            rooting it to the current crops page */}
                            {/* Do the titles not need reverse fragments? */}
                          </li>
                          </li>
                            Plant a Crop
                            // again, replaced by </li that will lead to 
                            // add a crop page
                          </li>
                          <li> 
                            Crop Maintenance
                          </li>
                        </>
                    )}
                </ul>
            </nav>
        </header>
    )
}

export default Header;