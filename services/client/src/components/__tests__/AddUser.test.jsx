import React from "react";
import {render,cleanup} from '@testing-library/react';

import AddUser from "../AddUser";

afterEach(cleanup);

it("renders with default props", () => {
 const {getByLabelText,getByText} = render(<AddUser
 username=""
 email = ""
 />);

 const usernameInput = getByLabelText('username')
 expect(usernameInput).toHaveAttribute('type','text')
 expect(usernameInput).toHaveAttribute('required')
 expect(usernameInput).not.toHaveValue();

 const emailInput = getByLabelText('email');
 expect(emailInput).toHaveAttribute('type','email');
 expect(emailInput).toHaveAttribute('required');
 expect(emailInput).not.toHaveValue();

 const buttonInput = getByText('Submit');
 expect(buttonInput).toHaveValue('Submit');
 });