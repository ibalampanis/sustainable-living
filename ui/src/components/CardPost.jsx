import React from 'react';
import {MDBContainer, MDBCard, MDBCardTitle, MDBCardBody, MDBCardImage} from 'mdb-react-ui-kit';
import {Col, Row} from "reactstrap";
import {getPosts} from "./posts";
import { useState } from 'react';
import "./CardPost.css";

export default function CardPost() {
    const [posts] = useState(getPosts());
    return (
                        <Row> 
                            {posts.map(post => (       
                        <Col sm="5" md ="5" lg="5" xl="3" key= {post.id}>
                            {console.log(post.content.length)}
                                <MDBContainer style={{width:"600px", padding:"50px"}}>
                                <MDBCard className="card-border">
                                    <MDBCardBody className="p-4">
                                        <div className="d-flex text-black">
                                            <div className="flex-shrink-0">
                                                <MDBCardImage
                                                    src={post.img}
                                                    alt="post_Img"
                                                    className="rounded-circle"
                                                    style={{ width: '150px', padding: "20px"}}
                                                    fluid />
                                            </div>
                                            <hr/>
                                            <div className="flex-grow-1 ms-3">
                                                <MDBCardTitle><h3>{post.title}</h3></MDBCardTitle>
                                                <div className="d-flex justify-content-start rounded-3 p-2 mb-2">
                                                    <div>
                                                        {post.content.map(line =>(
                                                            <p className="mb-0">{line}</p>
                                                        ))}
                                                    </div> 
                                                </div>
                                            </div>
                                        </div>
                                    </MDBCardBody>
                                </MDBCard>
                                </MDBContainer>
                        </Col>
                            ))}
                        </Row>


    );
}