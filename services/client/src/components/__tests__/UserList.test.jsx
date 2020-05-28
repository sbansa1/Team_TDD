import React from "react";
import {render,cleanup} from '@testing-library/react';
import UsersList from '../UsersList';

afterEach(cleanup);

const users = [ {
'email':'saurabh.bnss0123@gmail.com',
'username':'saurabh'},
{'email': 'madubala@gmail.com',
'username':',madubala'}
];

it('renders a username',() =>{
 const {getByText} = render(<UsersList users={users}/>);
 expect(getByText('saurabh')).toHaveClass('username');
});

it("renders",() => {
   const { asFragment } = render(<UsersList users={users}/>);
   expect(asFragment()).toMatchSnapshot();
});

