package com.b4u.tinyfacebook.controller.post;

import com.b4u.tinyfacebook.entity.Post;
import com.b4u.tinyfacebook.entity.ResultBean;
import org.springframework.context.annotation.Scope;
import org.springframework.web.bind.annotation.*;

import java.util.Date;

/**
 * Controller for post.
 * This class has been deprecated since v3.0 because the appearance of PostRepository.
 *
 * @author hzy
 * @since 1.0
 */
@Deprecated
@RestController
@RequestMapping("/v1/posts")
public class PostController {

    /**
     * query post by post id
     * @param postId post id
     * @return post
     */
    @RequestMapping(value="/{postId}", method= RequestMethod.GET)
    public ResultBean<Post> getPost(@PathVariable long postId) {
        Post post = new Post();
        post.setId(postId);
        post.setUsername("Tom");
        post.setContent("I am so happy today!");
        post.setCreateDate(new Date());
        return new ResultBean<Post>(post);
    }

    /**
     * save post
     * @return post id
     */
    @RequestMapping(value="/", method= RequestMethod.POST)
    public ResultBean<String> publishPost(@RequestBody Post post) {
        System.out.println("save post, post is " + post);
        return new ResultBean<>("id-1234567");
    }

    /**
     * change the group of the post
     * Use PUT beaause of idempotence.
     * No matter how many time you do the same change, the group of the post will always be the same .
     * @return post id
     */
    @RequestMapping(value="/{postId}/{group}", method= RequestMethod.PUT)
    public ResultBean changeGroup(@PathVariable String postId, @PathVariable String group) {
        System.out.println("change group, post id is " + postId + ", group is " + group);
        return new ResultBean();
    }

    @RequestMapping(value="/{postId}", method= RequestMethod.DELETE)
    public ResultBean deletePost(@PathVariable String postId) {
        System.out.println("delete post, post id is " + postId);
        return new ResultBean();
    }
}
