import { Module } from '@nestjs/common';
import { ScheduleModule } from '@nestjs/schedule';
import { ConfigModule } from '@nestjs/config';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { GithubJobModule } from './github-job/github-job.module';
import { TypeOrmModule } from '@nestjs/typeorm';
import { GithubRepo } from './github-job/entities/github-job.entity';

@Module({
  imports: [
    TypeOrmModule.forRoot({
      type: 'postgres',
      host: 'localhost',
      port: 5432,
      username: 'postgres',
      password: 'postgres',
      database: 'development',
      entities: [GithubRepo],
      synchronize: true,
    }),
    ScheduleModule.forRoot(),
    ConfigModule.forRoot({
      isGlobal: true,
    }),
    GithubJobModule
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
