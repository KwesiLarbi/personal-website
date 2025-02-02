import { Entity, PrimaryGeneratedColumn, Column, CreateDateColumn } from "typeorm";

@Entity()
export class GithubRepo {
    @PrimaryGeneratedColumn('uuid')
    id!: string;

    @Column()
    gh_id!: number;

    @Column()
    name!: string;

    @Column()
    html_url!: string;

    @Column()
    description!: string;

    @Column()
    created_at!: Date;

    @Column()
    updated_at!: Date;

    @Column()
    pushed_at!: Date;

    @Column()
    stargazers_count!: number;

    @Column()
    watchers_count!: number;

    @Column()
    programming_language!: string;

    @CreateDateColumn()
    db_creation_date!: Date;
}
