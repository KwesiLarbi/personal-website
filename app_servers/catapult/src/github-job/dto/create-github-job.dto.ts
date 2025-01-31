export class CreateGithubJobDto {
    id: string;
    gh_id: number;
    name: string;
    html_url: string;
    description: string;
    created_at: Date;
    updated_at: Date;
    pushed_at: Date;
    stargazers_count: number;
    watchers_count: number;
    programming_language: string;
}
