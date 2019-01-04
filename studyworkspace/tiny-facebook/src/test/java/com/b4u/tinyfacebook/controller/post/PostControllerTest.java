package com.b4u.tinyfacebook.controller.post;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;

import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

/**
 * @Author: hzy
 * @Description:
 * @Date: Created on 19:55 2017/10/16
 */

@RunWith(SpringRunner.class)
@SpringBootTest
@AutoConfigureMockMvc
public class PostControllerTest {
    @Autowired
    private MockMvc mvc;

    @Test
    public void getPost() throws Exception {
        mvc.perform(MockMvcRequestBuilders.get("/v1/posts/123").accept(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk());
    }
}
