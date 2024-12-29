export const config = {
    title: "Serena's Blog",
    favicon: "/avatar.jpg",
    subtitle: "Thoughts, stories, and ideas.",
    profileImage: "/avatar.jpg",
    links: [
        { name: "Home", href: "", match: "^/$" },
        { name: "Archive", href: "archive",  match: "^/archive|^/posts" },
        { name: "VRChat Memories", href: "gallery", match: "^/gallery" },
        { name: "About", href: "about", match: "^/about" },
    ]
};
